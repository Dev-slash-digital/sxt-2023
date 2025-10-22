export const useAPI = (request, opts) => {
    const config = useRuntimeConfig();
    const xsrfToken = useCookie("csrftoken");
    let headers = {
        accept: "application/json",
        ...opts?.headers,
    };
    headers["X-CSRFToken"] = xsrfToken;
    return useFetch(request, {
        baseURL: config.public.baseURL,
        headers,
        ...opts,
    });
};
