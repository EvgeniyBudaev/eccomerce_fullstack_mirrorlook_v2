import React, {useEffect} from 'react'
import {useDispatch, useSelector} from "react-redux"
import styles from './ProductList.module.scss'
import {fetchProductsByCatalog} from "../../../../../redux/actions/productListAction"

const ProductList = ({catalogSlug}) => {
    const dispatch = useDispatch()
    const productsList = useSelector(state => state.productList)
    const {loading, loaded, error, products} = productsList

    useEffect(() => {
        if (!loading[catalogSlug] && !loaded[catalogSlug]) {
            dispatch(fetchProductsByCatalog(catalogSlug))
        }
    }, [dispatch, catalogSlug, loading, loaded])
    console.log("products", products)

    return (
      <ul className={styles.productList}>
        {/*{products && products.map(product => <Card key={product.id} product={product} />)}*/}
      </ul>
    )
}

export default ProductList