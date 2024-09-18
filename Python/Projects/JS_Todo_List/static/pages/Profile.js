import store from "../utils/store.js";

const Profile = {
  template: `
    <div>
      <div v-if="allTodos.length === 0">
        No todos available.
      </div>
      <div v-else v-for="todo in allTodos" :key="todo.id">
        <h3>Title: {{ todo.title }}</h3>
        <p>Desc: {{ todo.desc }}</p>
        <p>Id: {{ todo.id }}</p>
        <p>User Id: {{ todo.user_id }}</p>
      </div>
    </div>
  `,

  data() {
    return {
      allTodos: [],
    }
  },

  async mounted() {
    const origin = store.state.origin;
    console.log("token: ", store.state.token);
    const res = await fetch(origin + '/api/todos', {
      headers: {
        "Authentication-Token": "store.state.token"
      },
    });
    const data = await res.json();
    this.allTodos = data;
  }

};

export default Profile;
