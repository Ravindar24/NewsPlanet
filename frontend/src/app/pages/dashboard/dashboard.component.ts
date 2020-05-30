import { Component, OnInit } from '@angular/core';
// import Chart from 'chart.js';
import { CovidService } from 'app/services/covid.service';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import { element } from 'protractor';

declare var $: any;
declare interface TableData {
  headerRow: string[];
  dataRows: string[][];
}

@Component({
  selector: 'dashboard-cmp',
  moduleId: module.id,
  templateUrl: 'dashboard.component.html'
})

export class DashboardComponent implements OnInit {

  states: string[] = [];

  public barChartOptions: ChartOptions = {
    responsive: true,
  };
  public barChartLabels: String[] = this.states;
  public barChartType: ChartType = 'bar';
  public barChartLegend = true;
  public barChartPlugins = [];


  public cummulativeData: any;
  public latestData: any;
  public loader: boolean;
  isFetchingStateData: boolean;
  isFetchingCountryData: boolean;
  tableHeaders: string[];
  stateWiseData: any[];
  statesBarChartData: any[];
  activeCases;


  public tableData1: TableData;

  prepareBarChartData(stateWiseData: any[]) {
    this.statesBarChartData = [{}];
    let active: number[] = [];
    let cases: number[] = [];
    let deaths: number[] = [];
    let recovered: number[] = [];

    stateWiseData.forEach(element => {
      active.push(element["active"]);
      cases.push(element["cases"]);
      deaths.push(element["deaths"]);
      recovered.push(element["recovered"]);
    });

    this.statesBarChartData.push(
      { data: active, label: 'Active', stack: 'a' },
      { data: cases, label: 'Cases', stack: 'a' },
      { data: deaths, label: 'Deaths', stack: 'a' },
      { data: recovered, label: 'Recovered', stack: 'a' }
    );
    this.statesBarChartData.splice(0, 1);
  }

  prepareTable(data: any[]) {
    let rows = [];
    data.forEach(element => {
      rows.push(element.id, element.name, element.confirmed, element.active, element.recovered, element.deaths)
    })

  }

  constructor(private covidService: CovidService) {
    this.tableHeaders = ["S.No", "State", "Confirmed", "Active", "Recovered", "Deaths"]
    this.getStatewiseData();
    this.getCoronaHistory();
  }

  getStatesNamesFromResponse(stateWiseData: any[]) {
    stateWiseData.forEach(element => {
      this.states.push(element["location"]);
    });
  }

  getStatewiseData() {
    this.isFetchingStateData = true;
    this.covidService.getStatewiseCovidData().subscribe(
      (response) => {
        this.isFetchingStateData = false;
        if (response) {
          this.stateWiseData = response["data"];
          this.getStatesNamesFromResponse(this.stateWiseData);
          this.prepareBarChartData(this.stateWiseData);
        }
      },
      (err) => {
        this.isFetchingStateData = false;
      })
  }

  getCoronaHistory() {
    this.isFetchingCountryData = true;
    this.covidService.getCountryCovidData().subscribe(
      (response) => {
        this.isFetchingCountryData = false;
        if (response) {
          this.cummulativeData = response["data"];
          this.latestData = this.cummulativeData[this.cummulativeData.length - 1]
          this.activeCases = this.latestData.Confirmed - (this.latestData.Recovered + this.latestData.Deaths)
        }
      },
      (err) => {
        this.isFetchingCountryData = false;
      }
    )
  }

  openFilterModal() {
    console.log("hi")
    $("#filterModal").modal('show');
  }


  ngOnInit() {

  }
}
