import StudyResource from "../components/StudyResource.js";

const DashboardStud = {
  template: `
        <div>
            <h1>this is student dashboard</h1>
            <div v-for="resource in allResource">
                <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
        </div>
    `,
  data() {
    return {
      allResource: [],
    };
  },
  async mounted() {
    const res = await fetch(window.location.origin + "/api/resources", {
      headers: {
        "Authentication-Token": sessionStorage.getItem("token"),
      },
    });
    const data = await res.json();
    this.allResource = data;
  },
  components: { StudyResource },
};

export default DashboardStud;
