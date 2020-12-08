import React, {useEffect, useState} from 'react';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import {getImage, getLabels, addLabels} from '../helpers/server';
import { Dialog, TextField, Button, DialogActions, DialogContent } from '@material-ui/core';

function Viewer() {
    const [viewImg, setViewImg] = useState(null);
    const [viewLabels, setViewLabels] = useState([]);
    const [open, setOpenForm] = useState(false);
    const [formValue, setFormValue] = useState("");
    const [triggerLabelReload,  setReload] = useState(0);

    useEffect(() => {
        const fetchData = async () => {
            const image = await getImage();
            setViewImg(image);
        }
        
        fetchData();
    }, []);

    useEffect(() =>{
        const fetchLabels = async () => {
            const labels = await getLabels();
            setViewLabels(labels)
        }
        
        fetchLabels();
    }, [triggerLabelReload])

    const handleOpen = () => {
        setOpenForm(true);
    }

    const handleSubmit = () =>{
        addLabels(formValue);
        setOpenForm(false);
        setReload(triggerLabelReload + 1);
    }
    const handleClose = () => {
        setOpenForm(false);
    };

    const handleChange = (event) => {
        setFormValue(event.target.value);
    };

    return (
        <div>
            {/* Input Image here */}
            <div>
                <img id="image" src={viewImg} alt="drawerImg"/>
            </div>

            <List>
                {
                    Object.keys(viewLabels||[]).map((key) => {
                        return(
                            <ListItem key={key}>
                                <ListItemText>{viewLabels[key]}</ListItemText>
                            </ListItem>
                        )
                    })
                }
            </List>
            <Fab color="primary" aria-label="add">
                <AddIcon onClick={handleOpen}/>
            </Fab>
            <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                <DialogContent>
                    <TextField id="outlined-basic" label="New Label" variant="outlined" onChange={handleChange}/>
                    
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">Cancel</Button>
                    <Button onClick={handleSubmit} color="primary">Submit</Button>
                </DialogActions>
                
            </Dialog>
            
        </div>
    );
}

export default Viewer;