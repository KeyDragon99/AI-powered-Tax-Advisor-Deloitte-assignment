import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/HomePage.vue";
import TaxFormPage from "./components/TaxFormPage.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/tax-form", component: TaxFormPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
