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
          console.log(response)
          console.log(this.countrySummary)

      },
      (err)=> {
        this.isFetchingCountrySummaryData = false;
      })

  }
}
