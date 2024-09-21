const Todo = {
    template: `
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
            <button @click="addTodo" type="submit" class="btn btn-primary">Submit</button>
        </div>
    `, 

    data() {
        return {
            title: "",
            desc: ""
        }
    },

    methods: {
        async addTodo() {
            const origin = this.$store.state.origin;
            const id = Number(sessionStorage.getItem("id"));
            const res = await fetch(origin + `/api/todos/${id}`, {
                method: "POST",
                headers: {
                    "Authentication-Token": sessionStorage.getItem("token"),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: this.title,
                    desc: this.desc
                })
            });
            if (res.ok) {
                console.log("todo created succesfully");
                const data = await res.json();
                console.log(data);
            }
        }
    }
}

export default Todo;
