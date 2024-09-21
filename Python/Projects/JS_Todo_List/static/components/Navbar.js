import router from "../utils/router.js";

const Navbar = {
    template: `
        <nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">TodoJS</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                    <router-link to="/" tag="a" class="nav-link">Home</router-link>
                    <router-link v-if="!state.loggedIn" to="/user-login" tag="a" class="nav-link">Login</router-link>
                    <router-link v-if="!state.loggedIn" to="/signup" tag="a" class="nav-link">Signup</router-link>
                    <router-link v-if="state.loggedIn" to="/profile" tag="a" class="nav-link">Profile</router-link>
                    <router-link v-if="state.loggedIn" to="/todo" tag="a" class="nav-link">Todo</router-link>
                </div>
                <div class="navbar-nav ms-auto">
                    <a v-if="state.loggedIn" @click="logout" class="nav-link text-danger fw-bold">Logout</a>
                </div>
                </div>
            </div>
        </nav>
    `,

    data() {
        return {
            url: this.$store.state.origin + '/logout'
        }
    },

    computed: {
        state() {
            return this.$store.state
        }
    },

    methods: {
        logout() {
            sessionStorage.clear();
            
            console.log(`Before clear ${this.$store.state.token}`)
            this.$store.commit('logout')
            console.log(`After clear ${this.$store.state.token}`)
            
            router.push('/');
        }
    }
};

export default Navbar;
