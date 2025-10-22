import API from "~/utils/axios";

export default defineNuxtRouteMiddleware(async (to, from) => {
    // get runtime configuration
    const config = useRuntimeConfig();
    // get the brand id
    const brand_id = from.params.brand_id;
    // check if the brand exists in the database
    try {
        await API.get(`${config.public.baseURL}/back/api/brands/${brand_id}/`);
    } catch (error) {
        // if the brand does not exist
        if (error.response.status === 404) {
            // return page not found error
            return abortNavigation();
        }
    }
    try {
        // get the email from cookies
        const email = useCookie("email").value;
        // if email is obtained then authenticate
        if (email !== undefined) {
            const data = {
                email,
                password: "",
            };
            // authenticate user
            const res = await API.post(
                `${config.public.baseURL}/back/api/user/me/`,
                data
            );
            // retrieve user authentication validator
            const isAuth = res.data.is_authenticated;
            // if user is not authenticated got to home
            if (!isAuth) {
                return navigateTo("/");
            }
        }
    } catch (error) {
        return navigateTo("/");
    }
});
