import { Component, OnInit } from '@angular/core';
import { CovidService } from 'app/services/covid.service';
import { ChartType, ChartOptions } from 'chart.js';
import { SingleDataSet, Label, monkeyPatchChartJsLegend, monkeyPatchChartJsTooltip } from 'ng2-charts';

@Component({
  selector: 'app-global',
  templateUrl: './global.component.html',
  styleUrls: ['./global.component.css']
})
export class GlobalComponent implements OnInit {
  isFetchingCountrySummaryData = false;
  countrySummary;
  activeCases;
  public canvas: any;
  public ctx;
  public globalCovidChart;
  isFetchingCountryData: boolean;
  tableHeaders: string[];
  countryWiseData: any[];


  public pieChartOptions: ChartOptions = {
    responsive: true,
  };
  public pieChartLabels: Label[] = ['Active', 'Recovered', 'Deaths'];
  public pieChartData: SingleDataSet;
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];


  constructor(private covidService: CovidService) {
    this.getCountrySummary();
    this.tableHeaders = ["S.No", "State", "Confirmed", "Recovered", "Deaths"]
    this.getCountrywiseDetailedData();
    monkeyPatchChartJsTooltip();
    monkeyPatchChartJsLegend();
  }

  ngOnInit(): void {
  }
  getCountrySummary() {
    this.isFetchingCountrySummaryData = true;
    this.covidService.getCountryCovideData().subscribe(
      (response) => {
        this.isFetchingCountrySummaryData = false;
        if (response)
          this.countrySummary = response;
        this.activeCases = this.countrySummary.TotalConfirmed - (this.countrySummary.TotalDeaths + this.countrySummary.TotalRecovered);
        this.preparePieDashboard();

      },
      (err) => {
        this.isFetchingCountrySummaryData = false;
      })

  }
  preparePieDashboard() {
    this.pieChartData = [this.activeCases, this.countrySummary.TotalRecovered, this.countrySummary.TotalDeaths,];
  }

  getCountrywiseDetailedData() {
    this.isFetchingCountryData = true;
    this.covidService.getCountryWiseDetailedCovideData().subscribe(
      (response) => {
        this.isFetchingCountryData = false;
        if (response) {
          this.countryWiseData = response["data"]
        }
      },
      (err) => {
        this.isFetchingCountryData = false;
      })
  }

}
