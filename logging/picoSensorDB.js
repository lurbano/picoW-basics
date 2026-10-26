class picoSensorDB {
    constructor(sensorID){
        this.sensorID = sensorID;
        this.fname = `pico_${sensorID}.json`;
    }

    fetchData(){
        fetch(this.fname, { cache: "no-cache" })
            .then(x => x.text())
            .then(y => this.processData(y));
            //.then(y => targetFunc(y));
    }

    processData(rawData){
        this.entries = []; //initialize array
        //split into lines
        rawData = rawData.split('\n');
        //parse each line as json
        for (let line of rawData){
            if  (line) { // if the line has information in it
                let d = JSON.parse(line);
                //console.log("d:", d);
                this.entries.push(d);
            }
        }
        //console.log(rawData.length);
        //console.log("this.entries:", this.entries);
        //targetFunc(rawData);
    }

    getTable(colName){
        //make html table
        let table = document.createElement("table");
        let dataset = this.get_td_array(colName);
        let head = table.createTHead();
        head.innerHTML = `<tr><td>time</td><td>${colName}</td></tr>`;

        for (let i=0; i<dataset.t.length; i++){
            let row = table.insertRow();

            //time
            let cell = row.insertCell();
            let t = new Date(dataset.t[i]*1000);
            cell.textContent = t.toLocaleString('en-us', { weekday:"short", year:"numeric", month:"short", day:"numeric", hour:"numeric", minute:"numeric", second:"numeric"});
            
            //data
            cell = row.insertCell();
            cell.textContent = dataset.d[i];
        }
        return table;
    }

    get_td_array(colName){
        let dataset = {
            t: [],
            d: []
        }
        for (let data of this.entries) {
            dataset.t.push(data['time']);
            dataset.d.push(data[colName]);
        }
        return dataset;
    }

}