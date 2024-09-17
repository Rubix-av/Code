import router from "../utils/router.js";

const Login = {
  template: `
        <div class="container mt-3" align="center" id="login-container">
            <div class="form-control mt-5">

                <h2 class="fw-bold" align="center">Login</h2> <br>

                <div class="form-floating mb-4">
                    <input v-model="email" type="email" id="email" name="email" placeholder="Enter Email" class="form-control">
                    <label for="email">Email : </label>
                </div>
                
                <div class="form-floating mb-3">
                    <input v-model="password" type="password" id="password" name="password" placeholder="Enter Password" class="form-control">
                    <label type="password">Password : </label>
                </div>
                <button @click="login" class="btn btn-primary" type="submit" id="login" style="width: 140px;">Login</button>
            </div>
        </div>
    `,

  data() {
    return {
      email: "",
      password: "",
    };
  },

  methods: {
    async login() {
      const url = window.location.origin;
      const res = await fetch(url + "/user-login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        }),
      });

      if (res.ok) {
        console.log("Login Successful!");
        router.push("/profile");
      } else {
        console.error("Login Failed!");
      }
    },
  },
};

export default Login;
