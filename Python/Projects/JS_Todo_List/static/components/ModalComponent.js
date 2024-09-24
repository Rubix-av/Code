const ModalComponent = {
  template: `
    <div class="modal">
      <div class="modal-content">
        <h2>{{ title }}</h2>
        <form @submit.prevent="submitForm">
          <label>Todo Title:</label>
          <input v-model="todo.title" type="text" />

          <label>Todo Description:</label>
          <input v-model="todo.desc" type="text" />

          <button type="submit" class="btn btn-primary">Update</button>
          <button @click="$emit('close')" class="btn btn-secondary">Cancel</button>'
        </form>
      </div>
    </div>
  `,
  props: {
    title: String,
    todo: Object,
  },
  methods: {
    submitForm() {
      this.$emit("submit", this.todo); // Emit the updated todo object
    },
  },
};

export default ModalComponent;
