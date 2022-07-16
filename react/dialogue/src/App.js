import React from 'react';
import logo from './logo.svg';
import './App.css';
// import ProgressBar from 'react-bootstrap/ProgressBar';
// import { MDBDataTable } from 'mdbreact';
// import {Tbl} from './Tbl';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      data: []
    }
  }
  componentDidMount() {
    var object = {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      }
    }

    fetch("http://localhost:8000/dialogue", object)
      .then((Response) => Response.json())
      .then((findresponse) => {
        console.log(findresponse)
        this.setState({
          count: findresponse.count,
          txt: findresponse.data
        });
      })
  }


  render() {
    console.log("state check", this.state.txt);
    return (
      <div className="App">
        <h3>{this.state.count} results found.</h3>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <table>
            <thead>

              <tr>
                <th>dialogues</th>
              </tr>
            </thead>
            <tbody>
              {this.state.txt  ? (this.state.txt.map(item => {
                return (<tr> <td>
                    {item._source.txt}  @ {item._source.from_time_txt}
                  </td>
                </tr>
                )
              })): (<tr> <td></td></tr>)}

            </tbody>
          </table>
        </header>
      </div>
    );
  }
}

export default App;
