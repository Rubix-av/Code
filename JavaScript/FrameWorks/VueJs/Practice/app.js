const dataObj = {
    count: 10000,
}

const optObject = {
    el: '#app',
    data: dataObj,
}

const app = new Vue(optObject)

setInterval(() => {
    app.$data.count -= 1
}, 1000)
