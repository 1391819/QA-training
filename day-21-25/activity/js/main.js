'use strict';

// selectors

let body = document.querySelector('body');
let table = document.querySelector('table');
let tableBody = document.querySelector('#table-body');

// functionality

// fetch data from the TFL API
const fetchData = () => {
	// API url
	const url = 'https://api.tfl.gov.uk/Line/Mode/tube/Status';

	axios
		.get(url)
		.then((response) => {
			// get original data
			const data = response.data;
			// filter only useful data - this could be done in the same block as displaying but modularity >>
			const filteredData = filterData(data);
			// displaying the filtered data
			displayData(filteredData);
		})
		.catch((err) => {
			console.error('Error fetching the data:', err);
			// just in case..
			const newP = document.createElement('p');
			newP.textContent = 'Error fetching the data..';
			body.appendChild(newP);
		});
};

const filterData = (data) => {
	// filter the data
	//     - we are only interested in name and statusSeverityDescription

	// array that will contain filtered objects
	let filteredData = [];

	for (let obj of data) {
		// recreate object with only name and statusSeverityDescription
		let filteredObject = {
			name: obj.name,
			statusSeverityDescription:
				obj.lineStatuses[0].statusSeverityDescription,
		};

		// append it to filtered objects array
		filteredData.push(filteredObject);
	}

	return filteredData;
};

const displayData = (data) => {
	// just letting the user know if there's no data available
	// not quite sure if this is needed (?)
	if (data.length == 0) {
		const newP = document.createElement('p');
		newP.textContent = 'No data..';
		body.appendChild(newP);
		return;
	}

	// making table visible
	table.style.display = 'table';

	// adding rows to the table contaning our filtered data - name and statusSeverityDescription
	data.forEach((element) => {
		const entryRow = document.createElement('tr');
		const td1 = document.createElement('td');
		const td2 = document.createElement('td');

		td1.textContent = element.name;
		td2.textContent = element.statusSeverityDescription;

		entryRow.appendChild(td1);
		entryRow.appendChild(td2);

		tableBody.appendChild(entryRow);
	});
};

// event listeners
window.addEventListener('load', fetchData); // load is not fired on document, but window
