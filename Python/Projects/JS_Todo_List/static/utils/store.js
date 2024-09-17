const store = new Vuex.Store({
    state: {
      origin: window.location.origin,
      token: "",
      role: "",
      email: "",
      id: ""
    },
    mutations: {
      setId(state, payload) {
        state.id = payload;
      },
      setEmail(state, payload) {
        state.email = payload;
      },
      setRole(state, payload) {
        state.role = payload;
      },
      setToken(state, payload) {
        state.token = payload;
      }
    }
  });
  
  export default store;
  