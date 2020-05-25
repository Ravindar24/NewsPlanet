import { Component, OnInit } from '@angular/core';
import { CovidService } from 'app/services/covid.service';
import Chart from 'chart.js';

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
  


  constructor(private covidService: CovidService) {
    this.getCountrySummary();
    this.tableHeaders = ["S.No", "State", "Confirmed", "Recovered", "Deaths"]
    this.getCountrywiseDetailedData();
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
        console.log(this.countrySummary.TotalConfirmed - (this.countrySummary.TotalDeaths + this.countrySummary.TotalRecovered));
        console.log(this.activeCases);
        this.preparePieDashboard();

      },
      (err) => {
        this.isFetchingCountrySummaryData = false;
      })

  }
  preparePieDashboard() {
    this.canvas = document.getElementById("globalCovidChart");
    this.ctx = this.canvas.getContext("2d");
    this.globalCovidChart = new Chart(this.ctx, {
      type: 'pie',
      data: {
        labels: [1, 2, 3],
        datasets: [{
          label: "Emails",
          pointRadius: 0,
          pointHoverRadius: 0,
          backgroundColor: [
            '#4acccd',
            '#28c26d',
            '#ef8157',
            '#fcc468'
          ],
          borderWidth: 0,

          data: [this.countrySummary.TotalConfirmed, this.countrySummary.TotalRecovered, this.countrySummary.TotalDeaths, this.activeCases]
        }]
      },

      options: {

        legend: {
          display: false
        },

        pieceLabel: {
          render: 'percentage',
          fontColor: ['white'],
          precision: 2
        },

        tooltips: {
          enabled: false
        },

        scales: {
          yAxes: [{

            ticks: {
              display: false
            },
            gridLines: {
              drawBorder: false,
              zeroLineColor: "transparent",
              color: 'rgba(255,255,255,0.05)'
            }

          }],

          xAxes: [{
            barPercentage: 1.6,
            gridLines: {
              drawBorder: false,
              color: 'rgba(255,255,255,0.1)',
              zeroLineColor: "transparent"
            },
            ticks: {
              display: false,
            }
          }]
        },
      }
    });

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
