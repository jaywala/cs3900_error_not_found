import axios from 'axios';
import AuthService from '../auth/AuthService';
const API_URL = 'http://localhost:8000';

export class APIService{
    constructor(){

    }

    /* The other methods go here */
    getAdvertisements() {
        const url = `${API_URL}/advertisement/`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }}).then(response => response.data);
    }
    getAdvertisement(pk) {
        const url = `${API_URL}/advertisement/${pk}`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }}).then(response => response.data);
    }
    getAdvertisementsByURL(link){
       const url = `${API_URL}${link}`;
       return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }}).then(response => response.data);
    }
    deleteAdvertisement(advertisement){
        const url = `${API_URL}/advertisement/${advertisement.pk}`;
        return axios.delete(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` }});
    }
    createAdvertisement(advertisement){
        const url = `${API_URL}/advertisement/`;
        const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.post(url,advertisement,{headers: headers});
    }
    updateAdvertisement(advertisement){
        const url = `${API_URL}/advertisement/${advertisement.pk}`;
        const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.put(url,advertisement,{headers: headers});
    }
}
