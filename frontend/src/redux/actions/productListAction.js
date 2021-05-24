import axios from "axios"
import {
    PRODUCT_LIST_FAILURE,
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS
} from "../../constants/productListConstants"

export const fetchProductsByCatalog = (catalog_slug) => async (dispatch) => {
    try {
        dispatch({type: PRODUCT_LIST_REQUEST, catalog_slug })
        const {data} = await axios.get(`/api/catalog/${catalog_slug}/`)
        dispatch({type: PRODUCT_LIST_SUCCESS, payload: data})
    } catch (error) {
        dispatch({type: PRODUCT_LIST_FAILURE, payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message
        })
    }
}