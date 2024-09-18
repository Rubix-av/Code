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
    const origin = this.$store.state.origin;
    console.log("token: ", this.$store.state.token);
    const res = await fetch(origin + '/api/todos', {
      headers: {
        "Authentication-Token": this.$store.state.token
      },
    });
    console.log("One")
    const data = await res.json();
    console.log("Two")
    this.allTodos = data;
  }
};

export default Profile;
