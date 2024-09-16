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
                        <router-link to="/login" tag="a" class="nav-link">Login</router-link>
                        <router-link to="/signup" tag="a" class="nav-link">Signup</router-link>
                        <router-link to="/profile" tag="a" class="nav-link">Profile</router-link>
                    </div>
                </div>
            </div>
        </nav>
    `,
};

export default Navbar;
