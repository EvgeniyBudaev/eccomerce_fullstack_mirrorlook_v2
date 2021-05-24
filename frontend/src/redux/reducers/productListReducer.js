import produce from 'immer'
import {
    PRODUCT_LIST_FAILURE,
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS
} from "../../constants/productListConstants"

const initialState = {
  loading: {},
  loaded: {},
  error: null,
  products: {},
}

export const productListReducer = (state = initialState, action) =>
  produce(state, (draft) => {
    // console.log('[productsReducer][action]', action)

    switch (action.type) {
      case PRODUCT_LIST_REQUEST: {
        draft.loading[action.catalogSlug] = true
        break
      }
      case PRODUCT_LIST_SUCCESS: {
        draft.loading[action.catalogSlug] = false
        draft.loaded[action.catalogSlug] = true
        draft.error = null
        draft.products[action.catalogSlug] = action.payload
        break
      }
      case PRODUCT_LIST_FAILURE: {
        draft.loading[action.catalogSlug] = false
        draft.loaded[action.catalogSlug] = false
        draft.error = action.payload
        break
      }
      default:
        return
    }
  })