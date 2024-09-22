const Profile = {
  template: `
    <div>
      <div v-for="(value, key, index) in userDetails" :key="index" class="container mt-1">
        <div class="accordion" :id="index + 'Example'">
          <div class="accordion-item">
            <h2 class="accordion-header" :id="'heading' + index">
              <button class="accordion-button" type="button" data-bs-toggle="collapse"
                :data-bs-target="'#collapse' + index" aria-expanded="true"
                :aria-controls="'collapse' + index">
                <strong>{{ key }}</strong>
              </button>
            </h2>
            <div :id="'collapse' + index" class="accordion-collapse collapse" 
                  :aria-labelledby="'heading' + index" :data-bs-parent="'#accordion' + index">
              <div class="accordion-body">
                {{ value }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,

  data() {
    return {
      userDetails: {},
    }
  },

  async mounted() {
    const origin = this.$store.state.origin;
    const user_id = sessionStorage.getItem('id');
    const token = sessionStorage.getItem('token');

    const res = await fetch(origin + `/api/users/${user_id}`, {
      headers: {
        "Authentication-Token": token,
        "Content-Type": "application/json"
      }
    });
    
    if (res.ok) {
      console.log("User data fetched successfully");
      const data = await res.json();
      this.userDetails = data;
    } else {
      console.log("Failed to fetch user data");
    }
  }
};

export default Profile;
