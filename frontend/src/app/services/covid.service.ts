import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { stateWiseCovidUrl, countryCovidUrl, countrySummary } from 'app/app.urls';

@Injectable({
  providedIn: 'root'
})
export class CovidService {

  constructor(private http: HttpClient) {

  }

  getStatewiseCovidData() {
    return this.http.get(stateWiseCovidUrl);
  }

  getCountryCovidData() {
    return this.http.get(countryCovidUrl);
  }

  getCountryCovideData() {
    return this.http.get(countrySummary);
  }
}
