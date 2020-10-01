import axios from 'axios'

const baseURL = '/api'

export default {
    async login(data) {
        return (await axios.post(`${baseURL}/accounts/login`, data))
    },
    async logout() {
        return (await axios.post(`${baseURL}/accounts/logout`))
    },
    async isLoggedIn() {
        return (await axios.get(`${baseURL}/accounts/islogin`)).data
    },
    async getMe() {
        return (await axios.get(`${baseURL}/accounts/mypage`)).data
    },
    async signup(data) {
        return (await axios.post(`${baseURL}/accounts/signup`, data))
    },
    async getDog(dogId) {
        return (await axios.get(`${baseURL}/details/${dogId}`)).data
    },
    async getDogs(data) {
        return (await axios.post(`${baseURL}/filters`, data))
    },
    async getScraps() {
        return (await axios.get(`${baseURL}//likes`)).data
    },
}
