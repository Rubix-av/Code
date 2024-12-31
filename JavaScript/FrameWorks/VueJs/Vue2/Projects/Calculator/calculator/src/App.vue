<!-- html -->
<template>
  <div id="app">
    <div class="calculator">

      <input v-model="input" id="input" type="text" readonly>

      <div class="row1" id="row">
        <button @click="clearInput" id="clear">C</button>
        <button @click="insertNum('(')" id="symbols">(</button>
        <button @click="insertNum(')')" id="symbols">)</button>
        <button @click="insertNum('/')" id="symbols">/</button>
      </div>

      <div class="row2" id="row">
        <button @click="insertNum('7')">7</button>
        <button @click="insertNum('8')">8</button>
        <button @click="insertNum('9')">9</button>
        <button @click="insertNum('+')" id="symbols">+</button>
      </div>

      <div class="row3" id="row">
        <button @click="insertNum('4')">4</button>
        <button @click="insertNum('5')">5</button>
        <button @click="insertNum('6')">6</button>
        <button @click="insertNum('-')" id="symbols">-</button>
      </div>

      <div class="row4" id="row">
        <button @click="insertNum('1')">1</button>
        <button @click="insertNum('2')">2</button>
        <button @click="insertNum('3')">3</button>
        <button @click="insertNum('*')" id="symbols">&times;</button>
      </div>

      <div class="row5" id="row">
        <button @click="backspace" id="delete">⌫</button>
        <button @click="insertNum('0')">0</button>
        <button @click="insertNum('.')">.</button>
        <button @click="calculate" id="equal">=</button>
      </div>

    </div>
  </div>
</template>

<!-- javascript -->
<script>
export default {
  data() {
    return {
      input: ""
    }
  },

  methods: {
    insertNum(digit) {
      this.input = this.input + digit;
    },

    clearInput() {
      this.input = "";
    },

    backspace() {
      try {
        this.input = this.input.slice(0, -1);
      } catch (error) {
        console.log("Error is: ", error);
      }
    },

    calculate() {
      try {
        this.input = eval(this.input);
      } catch (error) {
        this.input = "Error";
      }
    }
  },
}
</script>

<!-- css -->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

html {
  background-color: rgb(76, 72, 72);
}

#input {
  background-color: rgb(253, 244, 234);
  color: black;
  height: 35px;
  outline: 0;
  border: 0;
  border-radius: 2px;
  margin-bottom: 8px;
  text-align: center;
  font-weight: bold;
}

.calculator {
  background-color: rgb(18, 18, 18);
  display: flexbox;
  padding: 10px;
  width: fit-content;
  max-width: 540px;
  justify-content: center;
  margin: auto;
  border-radius: 7px;
}

#row {
  width: auto;
  display: flex;
  justify-content: space-between;
}

.calculator button {
  border: 0;
  outline: 0;
  width: 100%;
  height: 40px;
  margin: 2px;
  border-radius: 20px;
  background-color: rgb(30, 30, 30);
  color: white;
  font-weight: bold;
}

.calculator button:hover {
  cursor: pointer;
  background-color: rgb(56, 56, 56);
}

.calculator button:active {
  background-color: rgb(65, 65, 62);
}

#symbols {
  background-color: rgb(42, 104, 125);
}

#symbols:hover {
  opacity: 0.8;
}

#symbols:active {
  opacity: 0.5;
}

#clear {
  background-color: blueviolet;
}

#clear:hover {
  opacity: 0.8;
}

#clear:active {
  opacity: 0.5;
}

#equal {
  background-color: rgb(9, 58, 74);
}

#equal:hover {
  opacity: 0.8;
}

#equal:active {
  opacity: 0.5;
}

#delete {
  color: tomato;
  font-size: 25px;
}
</style>
