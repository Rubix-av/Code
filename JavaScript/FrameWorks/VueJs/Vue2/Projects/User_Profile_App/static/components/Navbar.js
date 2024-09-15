import store from "../utils/store.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link v-if="!loggedIn" to='/login'>Login</router-link>
    <router-link v-if="!loggedIn" to='/signup'>Signup</router-link>
    <router-link to='/dashboard'>Dashboard</router-link>
    <router-link to='/profile'>Profile</router-link>
    <a @click="logout">Logout</a>
    </nav>
    `,
  data() {
    return {
      loggedIn: store.state.loggedIn,
      url: window.location.origin + "/logout",
    };
  },
  
  computed: {
    computedLog(){
        return store.state.loggedIn;
    }
  },

  methods: {
    logout(){
        sessionStorage.clear();
        router.push('/home')
    }
  }
};

export default Navbar;
