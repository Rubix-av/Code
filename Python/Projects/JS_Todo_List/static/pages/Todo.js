const Todo = {
  template: `
        <div>
            <div class="container my-3">
                <h2>Add a Todo</h2>
                <!-- Todo Title -->
                <div class="mb-3">
                <label for="todoTitle" class="form-label">Todo Title</label>
                <input v-model="title" type="text" class="form-control" id="todoTitle" name="todoTitle" aria-describedby="emailHelp">
                </div>

                <!-- Todo Description -->
                <div class="mb-3">
                <label for="todoDesc" class="form-label">Todo Description</label>
                <input v-model="desc" type="text" class="form-control" id="todoDesc" name="todoDesc">
                </div>

                <!-- Submit Button -->
                <button @click="addTodo" type="submit" class="btn btn-primary fw-bold">Submit</button>
            </div>

            <div class="container my-3">
                <hr>
                <h2>Your Todos</h2>
                <div v-if="allTodos.length === 0" class="alert alert-warning text-center fs-3 mt-4">
                    <span><strong>Start Adding Todos</strong></span>
                </div>

                <table class="table">
                    <thead>
                        <th scope="col">#</th>
                        <th scope="col">Title</th>
                        <th scope="col">Description</th>
                        <th scope="col">Time</th>
                        <th scope="col">Result</th>
                    </thead>

                    <tbody>
                        <tr v-for="(todo, index) in allTodos" :key="todo.id">
                            <th scope="row">{{index+1}}</th>
                            <td>{{todo.title}}</td>
                            <td>{{todo.desc}}</td>
                            <td>{{todo.date_created}}</td>
                            <td>
                                <div class="btn-group" role="group" aria-label="DeleteDoneButtons">
                                <button type="button" class="btn btn-primary fw-bold">Update</button>
                                <div class="vh bold-and-thick"></div>
                                <button @click="deleteTodo(todo.id)" type="button" class="btn btn-danger fw-bold">Delete</button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    `,

  data() {
    return {
      title: "",
      desc: "",
      allTodos: [],
      showModal: false,
      selectedTodo: null,
    };
  },

  methods: {
    async addTodo() {
      const origin = this.$store.state.origin;
      const id = Number(sessionStorage.getItem("id"));
      const res = await fetch(origin + `/api/todos/${id}`, {
        method: "POST",
        headers: {
          "Authentication-Token": sessionStorage.getItem("token"),
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: this.title,
          desc: this.desc,
        }),
      });
      if (res.ok) {
        console.log("todo created succesfully");
        const data = await res.json();
        this.allTodos.push({
          id: data.todo_id,
          title: this.title,
          desc: this.desc,
          date_created: new Date().toLocaleString(),
        });

        this.title = "";
        this.desc = "";
      }
    },

    async deleteTodo(todoId) {
      const origin = this.$store.state.origin;
      const token = sessionStorage.getItem("token");

      const res = await fetch(origin + `/api/todos/${todoId}`, {
        method: "DELETE",
        headers: {
          "Authentication-Token": token,
        },
      });

      if (res.ok) {
        this.allTodos = this.allTodos.filter((todo) => todo.id !== todoId);
      } else {
        console.error("Failed to delete todo");
      }
    },
  },

  async mounted() {
    const origin = this.$store.state.origin;
    const user_id = sessionStorage.getItem("id");
    const token = sessionStorage.getItem("token");

    const res = await fetch(origin + `/api/todos/${user_id}`, {
      headers: {
        "Authentication-Token": token,
      },
    });

    console.log("One");
    const data = await res.json();
    console.log("Two");
    this.allTodos = data;
  },
};

export default Todo;
