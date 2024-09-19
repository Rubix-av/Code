const store = new Vuex.Store({
	state: {
    origin: window.location.origin,
    loggedIn: !!sessionStorage.getItem('token'), //sets value true/false based on token's presence
    token: sessionStorage.getItem('token') || "", //uses token value form sessionStorage if present else ""
		role: sessionStorage.getItem('role'),
		email: sessionStorage.getItem('email'),
    id: sessionStorage.getItem('id')
    },
    
    mutations: {
      setLogin(state) {
        state.loggedIn = true;
      },
      logout(state) {
        state.loggedIn = false;
        state.token = "";
      },
      setToken(state, payload) {
        state.token = payload
      }
    },
  });
  
  export default store;
  