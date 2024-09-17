import store from "../utils/store.js";

const Profile = {
  template: `
    <div>
      <h1>id: {{ id }}</h1>
      <h1>email: {{ email }}</h1>
      <h1>password: {{ password }}</h1>
      <h1>token: {{ token }}</h1>
    </div>
  `,
  computed: {
    id() {
      return store.state.id;
    },
    email() {
      return store.state.email;
    },
    password() {
      return store.state.password;
    },
    token() {
      return store.state.token;
    }
  }
};

export default Profile;
