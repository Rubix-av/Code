import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Profile from "../pages/Profile.js";

const routes = [
  { path: "/", component: Home },
  { path: "/user-login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/profile", component: Profile },
];

const router = new VueRouter({
  routes,
});

export default router;
