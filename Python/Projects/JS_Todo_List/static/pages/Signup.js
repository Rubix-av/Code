import router from "../utils/router.js";

const Signup = {
  template: `
        <div class="container mt-3" align="center" id="login-container">
            <div class="form-control mt-5">

                <h2 class="fw-bold" align="center">Signup</h2> <br>
                
                <select v-model="role" class="form-select form-floating mb-4" aria-label="Default select example" name="user_rank" required>
                    <option value="user">User</option>
                    <option value="admin">Admin</option>
                    <option selected value="" disabled>Login as...</option>
                </select>

                <div class="form-floating mb-4">
                    <input v-model="email" type="email" id="email" name="email" placeholder="Enter Email" class="form-control">
                    <label for="email">Email : </label>
                </div>
                
                <div class="form-floating mb-3">
                    <input v-model="password" type="password" id="password" name="password" placeholder="Enter Password" class="form-control">
                    <label type="password">Password : </label>
                </div>
                <button @click="signup" class="btn btn-primary" type="submit" id="login" style="width: 140px;">Signup</button>
            </div>
        </div>
    `,

  data() {
    return {
      email: "",
      password: "",
      role: "",
    };
  },

  methods: {
    async signup() {
      const url = window.location.origin;
      const res = await fetch(url + "/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
          role: this.role,
        }),
        credentials: "same-origin",
      });

      if (res.ok) {
        const data = await res.json();
        console.log("Signup Successful!");

        console.log(data);
        router.push("/user-login");
      } else {
        console.error("Signup Failed!");
      }
    },
  },
};

export default Signup;
