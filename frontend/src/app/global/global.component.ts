import { Component, OnInit } from '@angular/core';
import { CovidService } from 'app/services/covid.service';

@Component({
  selector: 'app-global',
  templateUrl: './global.component.html',
  styleUrls: ['./global.component.css']
})
export class GlobalComponent implements OnInit {
  isFetchingCountrySummaryData = false;
  countrySummary;
  activeCases;
  
  
  constructor(private covidService : CovidService) {     
  this.getCountrySummary();
  }

  ngOnInit(): void {
  }
  getCountrySummary() {
    this.isFetchingCountrySummaryData = true;
    this.covidService.getCountryCovideData().subscribe(
      (response) => {
        this.isFetchingCountrySummaryData = false;
        if(response)
          this.countrySummary = response;
          this.activeCases = this.countrySummary.TotalConfirmed - (this.countrySummary.TotalDeaths + this.countrySummary.TotalRecovered);
          console.log(this.countrySummary.TotalConfirmed - (this.countrySummary.TotalDeaths + this.countrySummary.TotalRecovered));
          console.log(this.activeCases);

      },
      (err)=> {
        this.isFetchingCountrySummaryData = false;
      })

  }
}
