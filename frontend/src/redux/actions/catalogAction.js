import axios from "axios"
import {
    CATALOG_FAILURE,
    CATALOG_REQUEST,
    CATALOG_SUCCESS
} from "../../constants/catalogConstants"

export const fetchCatalog = () => async (dispatch) => {
    try {
        dispatch({type: CATALOG_REQUEST})
        const {data} = await axios.get('/api/catalog/')
        dispatch({type: CATALOG_SUCCESS, payload: data})
    } catch (error) {
        dispatch({type: CATALOG_FAILURE, error: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message
        })
    }
}