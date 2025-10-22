import axios from "axios";

const API = axios.create({
    baseUrl: "",
    xsrfHeaderName: "X-CSRFToken",
    xsrfCookieName: "csrftoken",
    headers: {},
});

export default API;
