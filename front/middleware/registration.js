import API from "~/utils/axios";

export default defineNuxtRouteMiddleware(async (to, from) => {
    // get runtime configuration
    const config = useRuntimeConfig();
    // get the brand id
    const brand_id = to.params.brand_id;
    // check if the brand exists in the database
    try {
        await API.get(`${config.public.baseURL}/back/api/brands/${brand_id}/`);
    } catch (error) {
        // if the brand does not exist
        if (error.response && error?.response.status === 404) {
            // return page not found error
            return abortNavigation();
        }
    }
});
