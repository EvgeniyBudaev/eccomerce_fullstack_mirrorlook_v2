import React from 'react'
import {withRouter} from "react-router"

import styles from './CatalogContent.module.scss'
import ProductList from "./ProductList"

const CatalogContent = (props) => {
  // console.log('[CatalogContent][props]', props)

  const {catalogSlug} = props.match.params

  return (
    <div className={styles.catalogContent}>
      <ProductList catalogSlug={catalogSlug} />
    </div>
  )
}


export default withRouter(CatalogContent)