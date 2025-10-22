import API from "../utils/axios";

export default defineNuxtRouteMiddleware(async (to, from) => {
    const config = useRuntimeConfig();
    try {
        const res = await API.get(`${config.public.baseURL}/back/api/user/me/`);
        const isAuth = res.data.is_authenticated;
        const email = useCookie("email").value;
        if (isAuth && email !== undefined) {
            return navigateTo("/");
        }
    } catch (error) {
        console.log(error);
        return navigateTo("/");
    }
});
