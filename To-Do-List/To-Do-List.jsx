import { useState } from "react";

function Todo(){
    const[data,setData]=useState({task:"",status:"",deadline:""});
    const[active,setActive]=useState([]);
    const[edit,setEdit]=useState();

    const addToTask=()=>{
      if(edit!==null){
        const update=[...active];
        update[edit]=data;
        setActive(update);
        setEdit(null);
     } else{
        setActive([...active,data])
     }
     setData({
         task:"",
         status:"",
         deadline:""
     });
    };

    const remove=(ind)=>{
        let activeList=[...active];
        activeList.splice(ind,1);
        setActive(activeList);
    }
    const editTask=(ind)=>{
        setEdit(ind);
        const taskToEdit=active[ind];
        setData({
            task: taskToEdit.task,
            status: taskToEdit.status,
            deadline: taskToEdit.deadline
        });
    };
    return(
    <>
    <div className="main">
        <h1>TODO-LIST</h1>
      <form className="box">
      <h2>Add Task</h2>
        <div>
            <label>TASK</label><br></br>
             <input placeholder="Enter Task" value={data.task} name="task" onChange={(event)=>setData({...data,task:event.target.value})}/>
        </div><br></br>
        <div>
        <label>STATUS</label><br></br>
             <input placeholder="Enter Status" value={data.status} name="status" onChange={(event)=>setData({...data,status:event.target.value})}/>
        </div><br></br>
        <div id="date">
        <label>DEADLINE</label><br></br>
             <input  type="datetime-local" name="deadline" value={data.deadline} onChange={(event)=>setData({...data,deadline:event.target.value})}/>
        </div><br></br>
        <button type="button" onClick={()=>addToTask()}className="task">ADD TASK</button>
      </form><br></br>
      </div>
      <div>
      
      <table id="table">
        <caption><h2>Todo List</h2></caption>
        <thead id="head">
            <tr>
                <th>TASKS</th>
                <th>STATUS</th>
                <th>DEADLINE</th>
                <th>ACTION</th>
            </tr>
        </thead>
        <tbody>
            {active.map((value,ind)=>(
                <tr key={ind}>
                   <td>{value.task}</td>
                   <td>{value.status}</td>
                   <td>{value.deadline}</td>
                   <td>
                    <button className="edit" onClick={()=>editTask(ind)}>EDIT </button>
                    <button className="del" onClick={()=>remove(ind)}>DELETE</button>
                   </td>
                </tr>
            ))}
        </tbody>
      </table>
      </div>
    </>
    )
}
export default Todo; 