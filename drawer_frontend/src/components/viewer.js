import React, {useEffect, useState} from 'react';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import {getImage, getLabels} from '../helpers/server';

function Viewer() {
    const [viewImg, setViewImg] = useState(null);
    const [viewLabels, setViewLabels] = useState([]);
    useEffect(() => {
        const fetchData = async () => {
            const image = await getImage();
            setViewImg(image);

            const labels = await getLabels();
            setViewLabels(labels)
        }
        
        fetchData();
    }, []);

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
        </div>
    );
}

export default Viewer;