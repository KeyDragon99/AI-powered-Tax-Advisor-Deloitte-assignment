import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./components/HomePage.vue";
import TaxFormPage from "./components/TaxFormPage.vue";

const routes = [
  { path: "/", component: HomePage, meta: { title: "MTC Home" } },
  {
    path: "/tax-form",
    component: TaxFormPage,
    meta: { title: "MTC Tax Form" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Global navigation guard to update the page title
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || "Default Title";
  next();
});

export default router;
