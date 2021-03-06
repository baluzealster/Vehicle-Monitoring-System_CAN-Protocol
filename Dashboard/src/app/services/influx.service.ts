import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http'
import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
// import 'rxjs/Rx';



@Injectable({
  providedIn: 'root'
})
export class InfluxService {

  constructor(private http: Http) { }

  getData(chassiNo) {
    let body = {
      chassiNO: chassiNo
    }
    const header = new Headers();
    header.append("Content-Type", "application/json");
    return this.http
      .post('RESOURCE URL', body, { headers: header })
      .map(res => res.json());

  }


}
