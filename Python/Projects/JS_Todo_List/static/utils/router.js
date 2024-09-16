import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";

const routes = [
    {path:"/", component: Home},
    {path:"/login", component: Login},
    {path:"/signup", component: Signup}
]

const router = new VueRouter({
    routes
})

export default router;
