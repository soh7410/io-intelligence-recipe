<template>
  <div class="container">
    <h1>Recipe Generator</h1>
    <div
      v-for="(ingredient, index) in ingredients"
      :key="index"
      class="input-group"
    >
      <input
        v-model="ingredients[index]"
        placeholder="Enter ingredient"
        class="ingredient-input"
      />
      <button @click="removeIngredient(index)" v-if="ingredients.length > 1">
        -
      </button>
    </div>
    <button @click="addIngredient">+</button>
    <button @click="generateRecipe" :disabled="loading">Generate</button>

    <div v-if="loading" class="loading">Generating recipe...</div>

    <div v-if="recipe && !loading" class="recipe-output">
      <h2>Suggested Recipe</h2>
      <pre class="recipe-text">{{ recipe }}</pre>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      ingredients: ["", ""], // 最初から2つの入力欄を表示
      recipe: "",
      loading: false,
    };
  },
  methods: {
    addIngredient() {
      this.ingredients.push("");
    },
    removeIngredient(index) {
      this.ingredients.splice(index, 1);
    },
    async generateRecipe() {
      this.loading = true; // Start loading
      this.recipe = ""; // Clear previous recipe

      const API_ENDPOINT = "http://127.0.0.1:8000/generate-recipe/";

      try {
        const response = await axios.post(API_ENDPOINT, {
          ingredients: this.ingredients,
        });

        this.recipe = response.data.recipe
          .replace(/■/g, "\n■")
          .replace(/・/g, "\n・")
          .replace(/\d+\./g, "\n$&");
      } catch (error) {
        console.error("Recipe generation error:", error);
        this.recipe = "Recipe generation failed.";
      } finally {
        this.loading = false; // Stop loading
      }
    },
  },
};
</script>

<style>
.container {
  max-width: 500px;
  margin: auto;
  text-align: center;
}
.input-group {
  display: flex;
  justify-content: center;
  margin: 5px 0;
}
.ingredient-input {
  padding: 5px;
  width: 70%;
}
.input-group button {
  margin-left: 5px;
}
.loading {
  margin-top: 20px;
  font-weight: bold;
  color: blue;
}
.recipe-output {
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  white-space: pre-wrap; /* 改行を保持 */
  text-align: left;
}
.recipe-text {
  white-space: pre-wrap;
  line-height: 1.5;
}
</style>
