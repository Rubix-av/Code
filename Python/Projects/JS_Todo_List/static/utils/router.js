import store from "./store.js";

import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Profile from "../pages/Profile.js";
import Todo from "../pages/Todo.js";

const routes = [
  { path: "/", component: Home },
  { path: "/user-login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/profile", component: Profile, meta: { requiresLogin: true } },
  { path: "/todo", component: Todo, meta: { requiresLogin: true }}
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  if (!store.state.loggedIn && to.path !== "/user-login" && to.path !== "/" && to.path !== "/signup") {
    next({ path: "/user-login" });
  }
  else {
    next();
  }
})

export default router;
