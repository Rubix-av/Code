<template>
	<div>
		<button type="button" class="btn btn-primary">{{msg}}</button>
	</div>
</template>

<script>
import axios from 'axios';
export default {
	name: "Shark",
	data() {
		return {
			msg: "Hello, this is Shark"
		}
	},
	methods: {
		getResponse() {
			const path = 'http://localhost:5000/shark';
			axios.get(path)
				.then((res) => {
					console.log(res.data)
					this.msg = res.data;
				})
				.catch((e) => {
					console.error(e);
				})
		},
	},
	created() {
		this.getResponse();
	}
}
</script>