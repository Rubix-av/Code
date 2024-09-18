const store = new Vuex.Store({
    state: {
      origin: window.location.origin,
      loggedIn: false,
      token: sessionStorage.getItem('token'),
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
      },
    },
  });
  
  export default store;
  