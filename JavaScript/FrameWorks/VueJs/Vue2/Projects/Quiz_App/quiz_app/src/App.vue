<template>
  <div id="app">
    <h1>Simple Quiz</h1>
    <div class="quiz">
      <h2 id="question">Question goes here</h2>
      <div id="answer-buttons">
        <button class="btn">Answer 1</button>
        <button class="btn">Answer 2</button>
        <button class="btn">Answer 3</button>
        <button class="btn">Answer 4</button>
      </div>
      <button id="next-btn">Next</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [
        {
          question: "Which is the largest animal in the world",
          answers: [
            { text: "Shark", correct: false },
            { text: "Blue Whale", correct: true },
            { text: "Elephant", correct: false },
            { text: "Giraffe", correct: false }
          ]
        },
        {
          question: "Which is the smallest country in the world",
          answers: [
            { text: "Vatican City", correct: true },
            { text: "Bhutan", correct: false },
            { text: "Nepal", correct: false },
            { text: "Sri Lanka", correct: false }
          ]
        },
        {
          question: "Which is the largest desert in the world",
          answers: [
            { text: "Kalahari", correct: false },
            { text: "Gobi", correct: false },
            { text: "Sahara", correct: false },
            { text: "Antarctica", correct: true }
          ]
        },
        {
          question: "Which is the smallest continent in the world",
          answers: [
            { text: "Asia", correct: false },
            { text: "Australia", correct: true },
            { text: "Arctic", correct: false },
            { text: "Africa", correct: false }
          ]
        }
      ],

      question: "",
      answerButton: "",
    }
  },
  methods: {

  },
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: 'Poppins', 'sans-serif';
  box-sizing: border-box;
}

body {
  background: #001e4d;
}

#app {
  background: #fff;
  width: 90%;
  max-width: 600px;
  margin: 100px auto 0;
  border-radius: 10px;
  padding: 30px;
}

#app h1 {
  font-size: 25px;
  color: #001e4d;
  font-weight: 600;
  border-bottom: 1px solid #333;
  padding-bottom: 30px;
}

.quiz {
  padding: 20px 0;
}

.quiz h2 {
  font-size: 18px;
  color: #001e4d;
  font-weight: 600;
}

.btn {
  background: #fff;
  color: #222;
  font-weight: 500;
  width: 100%;
  border: 1px solid #222;
  padding: 10px;
  margin: 10px 0;
  text-align: left;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
}

.btn:hover {
  background: #222;
  color: #fff;
}

#next-btn {
  background: #001e4d;
  color: #fff;
  font-weight: 500;
  width: 150px;
  border: 0;
  padding: 10px;
  margin: 20px auto 0;
  border-radius: 4px;
  cursor: pointer;
  display: none;
}
</style>