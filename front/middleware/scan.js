import API from "../utils/axios";

export default defineNuxtRouteMiddleware(async (to, from) => {
    const config = useRuntimeConfig();
    let isAuth = false;
    try {
        const headers = useRequestHeaders(['cookie'])
        const res = await API.get(`${config.public.baseURL}/back/api/user/me/`, { headers: headers });
        isAuth = res.data.is_authenticated;
    } catch (error) {
        return navigateTo("/");
    }
    if (!isAuth) {
        const email = useCookie("email").value;
        if (email === undefined) {
            const tree_id = from.params.tree_id;
            return navigateTo(`/scan/${tree_id}/check/`);
        } else {
            try {
                const data = {
                    email: email,
                    password: "",
                };
                const res = await API.post(
                    `${config.public.baseURL}/back/api/user/me/`,
                    data
                );
                if (res.status !== 200) {
                    return navigateTo(`/scan/${tree_id}/check/`);
                }
            } catch (error) {
                if (
                    error.response.status === 404 &&
                    error.response.data?.detail === "Not found."
                ) {
                    const tree_id = from.params.tree_id;
                    return navigateTo(`/scan/${tree_id}/check/`);
                } else {
                    return navigateTo("/");
                }
            }
        }
    }
});
