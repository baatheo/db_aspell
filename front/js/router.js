import VueRouter from "vue-router";
import Home from "./views/Home";
import Upload from "./views/Upload";

const routes = [
    {
        path: "/",
        component: Home
    },
    {
        path: "/upload",
        component: Upload
    }
];

export default new VueRouter({
    routes,
    linkActiveClass: "is-active"
});
